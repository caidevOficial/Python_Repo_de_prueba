edad_usuario = 25

def validar_edad(edad):
    """
    Reciba una edad en formato string, valida que este formada por numeros y que 
    numericamente sea mayor o igual a 18. En caso de cumplir, 
    retorna la edad parseada a entero.
    """
    while not edad.isdigit() or (int(edad) < 18):
        edad = input(f'Ingrese la edad del cliente [Solo mayores de 18 años]: ')
    edad_int = int(edad)
    return edad_int





def restar(primer_numero: int, segundo_numero: int, multiplicar_por: int=2) -> int:
    """
    Toma dos numeros por parámetro, los resta entre si y al resultado lo multiplica por el numero
    del tercer parametro, por defecto es un 2
    
    Args:
        primer_numero: El primer operando de la función
        segundo_numero: El segundo operando de la función
    
    Returns:
        El resultado de la operación.
    """
    return (primer_numero - segundo_numero) * multiplicar_por


numero_a = 10.0
primer_numero=numero_a


numero_b = 5.0


print(
    restar(primer_numero=numero_a, segundo_numero=numero_b, multiplicar_por=3.0) 
)
