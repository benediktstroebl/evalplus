```python
def bf(planet1, planet2):
    """
    Returns a tuple of planets whose orbits are between the orbits of planet1 and planet2, 
    and are sorted by their proximity to the Sun.
    """return (j for j in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"] 
            if j == planet1 or j == planet2) and j in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus]
            else [planet1, planet2])

# Example usage:
print(bf("Mercury", "Uranus"))  # Output: ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
```