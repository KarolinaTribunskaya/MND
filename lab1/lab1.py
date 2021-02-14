import random

a0 = 1
a1 = 2
a2 = 3
a3 = 4

x1 = []
x2 = []
x3 = []

xn1 = []
xn2 = []
xn3 = []

for i in range(8):
    x1.append(random.randint(0, 20))
    x2.append(random.randint(0, 20))
    x3.append(random.randint(0, 20))

print(f"x1 = {x1}")
print(f"x2 = {x2}")
print(f"x3 = {x3}")

x1_min = min(x1)
x2_min = min(x2)
x3_min = min(x3)

x1_max = max(x1)
x2_max = max(x2)
x3_max = max(x3)

x01 = (x1_max + x1_min)/2
x02 = (x2_max + x2_min)/2
x03 = (x3_max + x3_min)/2

dx_1 = x1_max - x01
dx_2 = x2_max - x02
dx_3 = x3_max - x03

for i in range(len(x1)):
    xn1.append((x1[i] - x01)/dx_1)
    xn2.append((x2[i] - x02)/dx_2)
    xn3.append((x3[i] - x03)/dx_3)

y = []
for i in range(len(x1)):
    y.append(a0 + a1*x1[i] + a2*x2[i] + a3*x3[i])

print(f"\ny = {y}\n")

for i in range(len(x1)):
    xn1[i] = round(xn1[i], 3)
    xn2[i] = round(xn2[i], 3)
    xn3[i] = round(xn3[i], 3)

y_etalon = a0 + a1*x01 + a2*x02 + a3*x03


print(f"xn1 = {xn1}")
print(f"xn2 = {xn2}")
print(f"xn3 = {xn3}")



expression = []

for i in range(len(y)):
    expression.append((y[i] - y_etalon)**2)

print("\nx0 =", x01, x02, x03)
print("dx =", dx_1, dx_2, dx_3)

print(f"Еталонне значення y = {y_etalon}")

index_optimal = expression.index(max(expression))
print("Точка плану y(", x1[index_optimal], x2[index_optimal], x3[index_optimal], ") = ", y[index_optimal])
