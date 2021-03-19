def entrada():
    ladoa = float(input("Ingrese el valor del lado a: "))
    ladob = float(input("Ingrese el valor del lado b: "))
    ladoc = float(input("Ingrese el valor del lado c: "))

    while ladoa <= 0 or abs(ladoa) > abs(ladob) + abs(ladoc):
        ladoa = float(input("Ingrese el valor del lado a: "))

    while ladob <= 0 or abs(ladob) > abs(ladoa) + abs(ladoc):
        ladob = float(input("Ingrese el valor del lado b: "))

    while ladoc <= 0 or abs(ladoc) > abs(ladob) + abs(ladoa):
        ladoc = float(input("Ingrese el valor del lado c: "))


    return ladoa, ladob, ladoc