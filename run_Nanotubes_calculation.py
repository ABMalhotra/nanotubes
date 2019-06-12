from f2py_func import f2py_func

#USE PYTHON 3

# gfortran -c Silicon.f90
# f2py -c test1.f90 Silicon.f90 -m phonon_flight_library clear


Nk=100                 #k-Space discretization, larger values yield better convergence but require higher run-times.
Nr=16 				   #Real-Space discretization
Temperature=300.0      #in Kelvin
Dia_Outer=100.0*1e-9   #Outer diameter   
Dia_Inner=60.0*1e-9    #Inner diameter
Roughness_Outer=0.5*1e-9 #Roughness in nanometers
Roughness_Inner=0.5*1e-9
CL_Outer=10     #given as CL/eta i.e. Correlation length = CL_outer*eta
CL_Inner=10     #Correlation lengths
alloyPercent=0.0 #alloyed Ge percent 


ThermalConductivity,ThermalConductivityNTModes,NTModeCount=f2py_func.f2py_func(Nk=Nk,Nr=Nr,Temperature=Temperature,\
															Dia_Outer=Dia_Outer,Dia_Inner=Dia_Inner,Roughness_Outer=Roughness_Outer\
                                							,Roughness_Inner=Roughness_Inner,CL_Outer=CL_Outer,CL_Inner=CL_Inner,alloyPercent=alloyPercent)
print("")
print("******************RESULTS************************")
print( "Total K (W/m-K)    = {}".format(ThermalConductivity) )
print( "NTModes K (W/m-K)  = {}".format(ThermalConductivityNTModes) )
print( "#NTModes           = {}".format(NTModeCount) )

print("******************NANOTUBE***********************")
print( "shellThickness  (nm)  = {}".format( (0.5*Dia_Outer-0.5*Dia_Inner)*1e9 ) )
print( "Roughness_Inner (nm)  = {}".format( (Roughness_Inner)*1e9 ) )
print( "Roughness_Outer (nm)  = {}".format( (Roughness_Outer)*1e9 ) )

print("******************END OF RUN***********************")









