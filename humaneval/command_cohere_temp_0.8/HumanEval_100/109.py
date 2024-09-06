```python
def make_a_pile(n):
    # Get the next odd or even number based on the input being odd or even
    def get_next_num(input_num):
        return (input_num + 1) if input_num % 2 == 0 else (input_num + 2)
    
    # Generate the list of stone counts for each level
    num_list = [n]
    while len(num_list) < n:
        num_list.append(get_next_num(num_list[-1]))
    return num_list[:n]
```

This script defines a function `make_a_pile` that accepts a positive integer `n` as input and returns a list of stone counts for each level of the pile, ensuring that the problem statement's examples pass.