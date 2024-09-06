Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ate = n
    if need > rem:
        print("Oh oh, I'm going to eat everything that I have left...")
        need = rem
    print("I'm hungry, I'm going to eat...")
    for i in range(need):
        print("Bite {}!".format(i+1))
        ate += 1
    print("Yay, I'm full now!")
    return [ate, rem]
```

This code defines a function `eat` that takes three parameters: `n` (number of carrots already eaten), `need` (number of carrots needed to eat), and `rem` (the number of remaining carrots). The function starts by updating the `ate` variable to store the value of the number of carrots already eaten and checks if the remaining carrots are less than the number of carrots needed. If true, it informs the rabbit that it will eat everything left in the fridge and sets the need to the remaining amount. It then prints a message indicating that it is hungry and about to eat. It then iterates for the required number of bites (each bite increasing the ate counter by 1) and then prints a yay message indicating that it is now full. The function returns a list containing [ate, rem] which are the total number of carrots eaten after meals and the number of carrots left after meals respectively. 

The code uses python's built-in print function to print messages and the range function to assist in the iterative process. 

Note: The script's `eat` function includes some friendly messages and print instructions that are meant to make the code more readable and understandable. Feel free to remove these messages to make the code more efficient if needed.