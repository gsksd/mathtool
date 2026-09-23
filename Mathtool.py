# Лабораторная работа №1. "Решение уравнения"
# Консольное приложение решает уравнение вида A*x^2 + B*x + C = 0
MAX_ABS_VALUE = 10000

def read_coefficient(name):
    
    raw_value = input(f"Введите коэффициент {name}: ")

    try:
        value = int(raw_value)
    except ValueError:
        print("Неверный ввод: значение не является целым числом.")
        return None

    if abs(value) > MAX_ABS_VALUE:
        print(f"Неверный ввод: значение по модулю превышает {MAX_ABS_VALUE}.")
        return None

    return value


def solve_linear(b, c):
    
    print("Уравнение линейное: B*x + C = 0")

    if b == 0:
        if c == 0:
            print("Корнем уравнения является любое действительное число.")
        else:
            print("У уравнения нет корней.")
    else:
        x = -c / b  
        print(f"Корень уравнения: x = {x:.3f}")


def solve_quadratic(a, b, c):
    
    print("Уравнение квадратное: A*x^2 + B*x + C = 0")

    discriminant = b * b - 4 * a * c
    print(f"Дискриминант: D = {discriminant:.3f}")

    if discriminant > 0:
        sqrt_d = discriminant ** 0.5
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        print(f"Корни уравнения: x1 = {x1:.3f}, x2 = {x2:.3f}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"Корень уравнения: x = {x:.3f}")
    else:
        print("Действительных корней нет.")


def main():
    print("Решение уравнения вида: A*x^2 + B*x + C = 0")

    a = read_coefficient("A")
    if a is None:
        return

    b = read_coefficient("B")
    if b is None:
        return

    c = read_coefficient("C")
    if c is None:
        return

    if a == 0:
        solve_linear(b, c)
    else:
        solve_quadratic(a, b, c)

if __name__ == "__main__":
    main()
