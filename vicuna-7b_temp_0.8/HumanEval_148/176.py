
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
    if planet1 == "Mercury" or planet1 == "Venus" or \
       planet1 == "Earth" or planet1 == "Mars" or \
       planet1 == "Jupiter" or planet1 == "Saturn" or \
       planet1 == "Uranus" or planet1 == "Neptune":
        return tuple()
    elif planet2 == "Mercury" or planet2 == "Venus" or \
           planet2 == "Earth" or planet2 == "Mars" or \
           planet2 == "Jupiter" or planet2 == "Saturn" or \
           planet2 == "Uranus" or planet2 == "Neptune":
        return tuple()
    else:
        planets = [planet1, planet2]
        while len(planets) > 1:
            planet1, planet2 = planets[0], planets[1]
            if planet1 < planet2:
                break
            planets = [p for p in planets if p != planet1 and p != planet2]
        return tuple(sorted(planets, key=lambda p: (p.get_distance_to_sun() - planet2.get_distance_to_sun())))
