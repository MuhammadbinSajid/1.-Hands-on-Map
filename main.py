#using map
nums = [1, 2, 3, 4, 5]
def sq(n):
    return n*n
square = list(map(sq, nums))
print("Square of number sin list")
print(square)