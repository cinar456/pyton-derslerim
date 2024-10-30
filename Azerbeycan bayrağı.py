import turtle

# Ekran ayarları
window = turtle.Screen()
window.title("Azerbaycan Bayrağı")
window.setup(width=800, height=600)

# Turtle ayarları
t = turtle.Turtle()
t.speed(10)

# Kırmızı arka plan (orta şerit)
t.penup()
t.goto(-300, 100)
t.pendown()
t.color("red")  # Kırmızı renk
t.begin_fill()
for _ in range(2):
    t.forward(600)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

# Mavi üst şerit
t.penup()
t.goto(-300, 200)
t.pendown()
t.color("blue")  # Mavi renk
t.begin_fill()
for _ in range(2):
    t.forward(600)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()

# Yeşil alt şerit
t.penup()
t.goto(-300, -100)
t.pendown()
t.color("green")  # Yeşil renk
t.begin_fill()
for _ in range(2):
    t.forward(600)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()

# Ayın Çizimit.penup()
t.goto(-50, 0)
t.setheading(90)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(80)
t.end_fill()

# İç ay çizimi (kırmızı)
t.penup()
t.goto(-30, 0)
t.setheading(90)
t.pendown()
t.color("#ED2939")
t.begin_fill()
t.circle(60)
t.end_fill()

# Yıldız çizimi fonksiyonu
def draw_star(x, y, size):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    for _ in range(8):  # Sekiz köşeli yıldız
        t.forward(size)
        t.right(135)
    t.end_fill()
    t.penup()

# Yıldızın çizilmesi
t.color("white")
draw_star(50, 30, 40)  # Yıldızın boyutunu ve konumunu ayarla

# İşlem tamamlandıktan sonra pencereyi kapatmak için tıklamayı bekleme
t.hideturtle()
window.exitonclick()