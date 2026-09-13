def decimal_a_binario():
    while True:
        entrada = input("Ingresa un número decimal (de tres digitos: ").strip()

        # Validación: debe ser numérico entero y tener como máximo 3 dígitos
        if entrada.isdigit() and len(entrada) <= 3:
            numero = int(entrada)
            break
        else:
            print("Error: Ingresa un número entero positivo de hasta 3 cifras.\n")

    # Caso base: el 0 en binario es 0
    if numero == 0:
        binario = "0"
    else:
        bits = []
        n = numero
        while n > 0:
            bits.append(str(n % 2))
            n //= 2
        # Los residuos se leen en orden inverso
        binario = "".join(reversed(bits))

    print(f"\nEl equivalente binario de {numero} es: {binario}")


if __name__ == "__main__":
    decimal_a_binario()