#Estados permitidos:
#   sleep
#   run
#   finish

programadorA  = "sleep"
programadorB  = "sleep"
tester = "sleep"
analista = "run"
disenador = "run"

t=0



#####################################################################
def logicaAnalista(analista):
    
    if (analista == "run") :
        print("Analista termina proceso")
        return "finish"
    
    if (analista == "finish") :
        print("Analista en espera de tester")
        return "sleep"
        
    if (tester == "finish") :
        print("Analista inicia")
        return "run"
        
    if (analista == "sleep") :
        print("Analista en espera de tester")
        return "sleep"
###################################################################   
def logicaDisenador(disenador):
    if (disenador == "run") :
        print("Disenador termina proceso")
        return "finish"
    
    if (disenador == "finish") :
        print("Disenador en espera de tester")
        return "sleep"
        
    if (tester == "finish") :
        print("Disenador inicia")
        return "run"
        
    if (disenador == "sleep") :
        print("Disenador en espera de tester")
        return "sleep"
##################################################
def logicaTester(programadorA , programadorB):
    
    if (tester == "run") :
        print("Tester termina proceso")
        return "finish"
        
    if (tester == "finish") :
        print("Tester espera de Programadores")
        return "sleep"
        
    if (programadorA == "finish" and programadorB == "finish") :
        print("Tester inicia")
        return "run"
        
    if (tester == "sleep") :
        print("Tester en espera de Programadores")
        return "sleep"
#####################################################
def logicaProgramadorA(analista,  disenador):
    if (programadorA == "run") :
        print("ProgramadorA termina proceso")
        return "finish"
    
    if (programadorA == "finish") :
        print("ProgramadorA en espera de tester")
        return "sleep"
    
    if (analista == "finish" and disenador == "finish"):
        print("ProgramadorA inicia")
        return "run"
        
    if (programadorA == "sleep") :
        print("ProgramadorA en espera de tester")
        return "sleep"
#######################################################
def logicaProgramadorB(analista,  disenador):
    if (programadorB == "run") :
        print("ProgramadorB termina proceso")
        return "finish"
    
    if (programadorB == "finish") :
        print("ProgramadorB en espera de tester")
        return "sleep"
    
    if (analista == "finish" and disenador == "finish") :
        print("ProgramadorB inicia")
        return "run"
        
    if (programadorB == "sleep") :
        print("ProgramadorB en espera de tester")
        return "sleep"
#####################################################
    

while t<10:
    print(t,"##################################################")
    analista = logicaAnalista(analista)
    disenador = logicaDisenador(disenador)
    programadorA = logicaProgramadorA(analista, disenador)
    programadorB  = logicaProgramadorB(analista, disenador)
    tester = logicaTester(programadorA, programadorB)
    t +=1