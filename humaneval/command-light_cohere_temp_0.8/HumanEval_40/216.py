```python
def triples_sum_to_zero(l: list):
    return any(sum(x) <= 0 for x in l)

# Example usage
if __name__ == "__main__":
    input = [1, 3, 5, 0]
    output = triples_sum_to_zero(input)
    print(output)  # Output should be True
```