```python
def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represents the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    """
    string s = input("Enter string representing the number of apples and oranges: ")
    string s = input().RC("Enter an integer n representing the total number of fruits, then enter apples and oranges separated by spaces: ").
    n = int(input("Enter an integer n representing the total number of fruits: "))
    s = input("Enter the number of apples: ")
    s = input("Enter the number of oranges: ")
    return n - s - o

# test
if __name__ == "__main__":
    n = int(input("Enter an integer n representing the total number of fruits: "))
    print("The number of mango fruits in the basket: " + fruit_distribution(input("Enter a string representing the number of apples and oranges: "),n))
```