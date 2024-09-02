
def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    fruits = []
    for letter in s:
        if letter == "a":
            fruits.append(1)
        elif letter == "o":
            fruits.append(0)
        elif letter == "m":
            fruits.append(1)
        else:
            print("Invalid fruit")
            return -1
    sum_apples = 0
    sum_oranges = 0
    for i in range(len(fruits)):
        if fruits[i] == 1:
            sum_apples += 1
        else:
            sum_oranges += 1
    total_fruits = sum_apples + sum_oranges
    if sum_apples == n and sum_oranges == n:
        return -1
    else:
        return total_fruits - n

n = int(input("Enter total number of fruits in the basket: "))
fruits = fruit_distribution(s,n)
if fruits > 0:
    print("There are", fruits, "mango fruits in the basket.")
else:
    print("There are no mango fruits in the basket.")