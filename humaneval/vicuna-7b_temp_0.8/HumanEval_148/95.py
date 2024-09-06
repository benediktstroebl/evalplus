
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
    # TODO: implement the function
    if planet1.lower() != "earth" and planet1.lower() != "venus" and planet1.lower() != "mars" and planet1.lower() != "jupiter" and planet1.lower() != "saturn":
        if planet2.lower() != "earth" and planet2.lower() != "venus" and planet2.lower() != "mars" and planet2.lower() != "jupiter" and planet2.lower() != "saturn":
            return tuple()
        else:
            planets = tuple(sorted(list(zip(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"], [planet1.lower(), planet2.lower()])))[1])
            return planets
    else:
        if planet1.lower() != "earth" and planet1.lower() != "venus" and planet1.lower() != "mars" and planet1.lower() != "jupiter" and planet1.lower() != "saturn":
            return tuple()
        else:
            planets = tuple(sorted(list(zip(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"], [planet1.lower(), planet2.lower()])))[1])
            return planets
