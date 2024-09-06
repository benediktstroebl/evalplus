
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"] or planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    elif planet1 < planet2:
        return (planet1,) + sorted((planet2,) + list(range(planet1+1, len(planet2)+1)))
    elif planet1 > planet2:
        return (planet2,) + sorted((planet1,) + list(range(planet2+1, len(planet1)+1)))
    elif planet1 == planet2:
        return ()
    else:
        return (planet1, planet2)

planet1 = input("Enter the name of the first planet: ")
planet2 = input("Enter the name of the second planet: ")
result = bf(planet1, planet2)
print(*result, sep='\n')