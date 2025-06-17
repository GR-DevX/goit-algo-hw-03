import turtle

def koch_curve(t: turtle.Turtle, order: int, size: float):
    """
    Малює сегмент кривої Коха.

    Args:
        t (turtle.Turtle): Об'єкт turtle для малювання.
        order (int): Рівень рекурсії.
        size (float): Довжина сегмента.
    """
    if order == 0: # Базовий випадок рекурсії [cite: 35]
        t.forward(size)
    else: # Рекурсивний випадок [cite: 36]
        # Кожен сегмент ділиться на 4 менших з відповідними поворотами
        # Це відповідає класичному побудуванню кривої Коха, де середній сегмент замінюється "шипом"
        # Див. опис побудови фракталів [cite: 56] та приклад кривої Коха [cite: 152, 153]
        size_third = size / 3.0
        koch_curve(t, order - 1, size_third)
        t.left(60)
        koch_curve(t, order - 1, size_third)
        t.right(120)
        koch_curve(t, order - 1, size_third)
        t.left(60)
        koch_curve(t, order - 1, size_third)

def draw_koch_snowflake(order: int, size: float = 300.0):
    """
    Малює сніжинку Коха, яка складається з трьох кривих Коха.
    """
    window = turtle.Screen()
    window.bgcolor("white")
    window.setup(width=800, height=600)

    t = turtle.Turtle()
    t.speed(0)  # Найвища швидкість
    t.hideturtle()
    t.penup()
    # Позиціонування для центрування сніжинки
    t.goto(-size / 2, size / (2 * (3**0.5))) # Приблизний центр для рівностороннього трикутника
    t.pendown()
    t.pencolor("blue")

    for _ in range(3): # Сніжинка Коха складається з 3-х кривих Коха [cite: 154]
        koch_curve(t, order, size)
        t.right(120) # Поворот для наступної сторони сніжинки

    window.mainloop()

def main():
    while True:
        try:
            recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха (наприклад, 0-5): "))
            if recursion_level < 0:
                print("Рівень рекурсії не може бути від'ємним. Спробуйте ще раз.")
            else:
                break
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    draw_koch_snowflake(recursion_level)

if __name__ == "__main__":
    main()
