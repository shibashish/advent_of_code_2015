with open('input.in.txt') as file:
    data = [i for i in file.read().strip().split("\n")]


def sorted_sides(x):
    x = x.split("x")
    sides = [int(i) for i in x]
    sides.sort()
    return sides

def calculate_total(input):
    total_area = 0
    ribbon_total = 0
    for i in input:
        s = sorted_sides(i)
        area = (2*s[0] * s[1]) + (2*s[1]*s[2]) + (2*s[2]*s[0]) + (s[0] * s[1])
        ribbon = s[0] + s[0] + s[1] + s[1] + (s[0] * s[1] * s[2])
        total_area = total_area + area
        ribbon_total = ribbon_total + ribbon
    return total_area , ribbon_total

total_area , ribbon_total = calculate_total(data)

print (f"Total paper required is : {total_area}")
print(f"Total ribbon required is : {ribbon_total}")
