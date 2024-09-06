
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
    if planet1 == "Jupiter" or planet2 == "Jupiter":
        return tuple(sorted(list(set(planet1.split(" ")) & set(planet2.split(" ")))))
    elif planet1 == "Saturn" or planet2 == "Saturn":
        return tuple(sorted(list(set(planet1.split(" ")) - set(planet2.split(" ")))))
    elif planet1 == "Uranus" or planet2 == "Uranus":
        return tuple(sorted(list(set(planet1.split(" ")) - set(planet2.split(" "))))[::-1])
    elif planet1 == "Neptune" or planet2 == "Neptune":
        return tuple(sorted(list(set(planet1.split(" ")) - set(planet2.split(" "))))[::-1])
    elif planet1 == "Venus" or planet2 == "Venus":
        return tuple(sorted(list(set(planet1.split(" ")) & set(planet2.split(" "))))[::-1])
    elif planet1 == "Mars" or planet2 == "Mars":
        return tuple(sorted(list(set(planet1.split(" ")) & set(planet2.split(" ")))))
    elif planet1 == "Earth" or planet2 == "Earth":
        return tuple(sorted(list(set(planet1.split(" ")) & set(planet2.split(" "))))[::-1])
    else:
        return tuple()

planet1 = input("Enter first planet name: ")
planet2 = input("Enter second planet name: ")
result = bf(planet1, planet2)
