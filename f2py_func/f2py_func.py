def f2py_func(Nk=100,Nr=16,Temperature=300.0,Dia_Outer=100.0*1e-9,Dia_Inner=60.0*1e-9,Roughness_Outer=0.5*1e-9\
                                ,Roughness_Inner=0.5*1e-9,CL_Outer=10,CL_Inner=10,alloyPercent=0.0):


  import time
  import subprocess
  import sys
  import numpy as np
  subprocess.call(['clear'])
  print("")
  f2py_doc_string="     \n \
                              ********** (c) 2018 Georgia Institute of Technology *********\n \
                        =======================================================================\n \
                                                 Written by Abhinav Malhotra \n \
                                 For suggestions/bugs, write to abhinavemailid@gmail.com \n \
                                            or visit www.maldovan.gatech.edu \n \
                        =======================================================================\n \
                    Free use/distribution for academic use if citing Github repo and publication, see details at: \n \
                                        www.github.gatech.edu/amalhotra40/nanotubes \n \
                        =======================================================================\n "
  from nanotube_fortlibs import ntl as calc
  calc.__doc__=f2py_doc_string
  print(calc.__doc__)
  time.sleep(5)
  print("Starting with FORTRAN calculations...")
  ktot,knt,ntmodes=calc.getnanotubeconductivity(nk=Nk,nr=Nr,temp=Temperature,diameter_out=Dia_Outer,diameter_in=Dia_Inner,rparamout=Roughness_Outer*1e9\
                                ,rparamin=Roughness_Inner*1e9,cl_by_eta_out=CL_Outer,cl_by_eta_in=CL_Inner,ydefects=alloyPercent/100.0)
  subprocess.call(['rm','fort.102'])
  return (ktot,knt,ntmodes)      
          