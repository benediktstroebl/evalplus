```python
def make_a_pile(n):
    """
    Given a positive integer n, make a pile of n levels of stones. Each level has n stones, 
    with the number of stones in the next level determined by the formula:
    next_odd = 2 if n % 2 == 0 else 1
    return [i + 1 for i in range(n + 1) if i < n/2 else next_odd]

if __name__ == "__main__":
    n = int(input("Enter the number of stones: "))
    result = make_a_pile(n)
    print("The pile is:", result)
```
The function make_a_pile creates a list with each element equal to the number of stones in the level (i+1). The function then returns this list.