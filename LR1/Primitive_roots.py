import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def find_primitive_roots(p):
    print(f"\nЭтап 1 - проверяем является ли {p} простым числом")
    if not is_prime(p):
        print(f"Число {p} не является простым, а модуль p обязан быть простым числом!")
        return []
    print(f"Число {p} - простое => ищем первообразные корни\n")


    print("Этап 2 - находим все числа, которые могут быть первообразными корнями")
    print(f"Будут проверены все числа от 2 до {p-1}\n")


    def is_primitive_root(g, p):
        print(f"Проверяем число {g}:")
        powers = set()
        for k in range(1, p):
            power = pow(g, k, p)
            print(f"Вычисляем {g}^{k} mod {p} = {power}")
            if power in powers:
                print(f"Число {g} не является первообразным корнем, т.к. {power} повторяется!")
                return False
            powers.add(power)
        if len(powers) == p - 1:
            print(f"Число {g} - первообразный корень по модулю {p}")
            return True
        return False

    print("Этап 3 - проверяем каждого кандидата")
    primitive_roots = []
    for g in range(2, p):
        if is_primitive_root(g, p):
            primitive_roots.append(g)
        print()

    print("Этап 4 - выводим результат")
    if primitive_roots:
        print(f"Первообразные корни по модулю {p}: {primitive_roots}")
    else:
        print("Первообразные корни не найдены.")

    return primitive_roots


p = int(input("Введите число p: "))

roots = find_primitive_roots(p)