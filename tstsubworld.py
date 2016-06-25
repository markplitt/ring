from neuron import h
pc = h.ParallelContext()
pc.subworlds(2) # one subworld 
            # eg: if we ran this with 3 hosts, rank of subworld = 3

s =  'world' + str((pc.id_world(), pc.nhost_world()))+ ' bbs'+ str((pc.id_bbs(), pc.nhost_bbs())) \
 +' net'+ str((pc.id(),  pc.nhost()))
print s

from ring import runring

pc.runworker()

for ncell in range(5, 10):
  pc.submit(runring, ncell, 1, 100)

while (pc.working()):
  print pc.pyret()

pc.done()
h.quit()
