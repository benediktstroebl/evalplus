
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
    # your code here
    planets = []
    pl_names = {"Mercury": "Venus", "Venus": "Earth", "Earth": "Mars",
                "Mars": "Jupiter", "Jupiter": "Saturn", "Saturn": "Uranus", "Uranus": "Neptune"}
    for name in pl_names.keys():
        if planet1 == name:
            planets.append(pl_names[name])
        elif planet2 == name:
            planets.append(pl_names[name])
    return tuple(sorted(planets))

