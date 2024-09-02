
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
    planets = [("Mercury", 0.39), ("Venus", 0.72), ("Earth", 1), ("Mars", 1.52), ("Jupiter", 5.2), ("Saturn", 9.54), ("Uranus", 19.19), ("Neptune", 30.06)]
    planet_list = []
    for planet in planets:
        if planet1 == planet[0] or planet2 == planet[0]:
            planet_list.append(planet)
    planet_list.sort(key=lambda x:x[1])
    planet_list = [x[0] for x in planet_list]
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        return tuple(planet_list[planet_list.index(planet1):planet_list.index(planet2)+1])
