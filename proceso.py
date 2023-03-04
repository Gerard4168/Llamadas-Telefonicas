# Llamadas telefonicas

print("--------------------------------------------------")
print("------------Cuanto duro la llamada----------------")
print("--------------------------------------------------")

#input

t= int(input("Digite el valor de t: "))

#Procesing

if t<=3 : 
    rta = " de 300"
    print("El valor de la llamada es" + str(rta))
else:
    
    if t>3 :
     r= 300 + 50 * (t - 3 )

    print("El valor de la llamada es " + str(r))
 
