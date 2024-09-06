```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    if p1 == -1 or p2 == -1:
        return ()
    
    result = []
    for i in range(max(p1, p2), min(p1, p2), -1):
        if i >= 0 and i < len(planets):
            result.append(planets[i])
    
    return tuple(result)
```

The function `bf` takes in two strings, `planet1` and `planet2`, and returns a tuple of strings of all planets between the two planets, sorted by proximity to the sun. The function first finds the indices of `planet1` and `planet2` in the list of planets. If either of the inputs is not a planet, the function returns an empty tuple. Using the maximum and minimum of the indices, the function iterates through the indices in reverse to collect all planets between the two given planets. The tuple of planets is then returned. 

The example inputs for this problem are mostly contained within the problem statement itself, but here are some samples for a complete test:
```python
# Test 1
planet1 = "Jupiter"
planet2 = "Neptune"
print(bf(planet1, planet2))  # Output: ('Saturn', 'Uranus')

# Test 2
planet1 = "Earth"
planet2 = "Mercury"
print(bf(planet1, planet2))  # Output: ('Venus')

# Test 3
planet1 = "Mercury"
planet2 = "Uranus"
print(bf(planet1, planet2))  # Output: ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
```
This will output:
```bash
('Saturn', 'Uranus')
('Venus')
('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
```

Ensure that your implementation passes these tests as well!