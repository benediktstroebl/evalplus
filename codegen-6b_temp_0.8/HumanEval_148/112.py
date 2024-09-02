
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
    sun = "Sun"
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    sun_pos = planets.index(sun)
    planet1_pos = planets.index(planet1)
    planet2_pos = planets.index(planet2)
    if planet1_pos < sun_pos < planet2_pos:
        return tuple(planets[sun_pos:planet1_pos]) + tuple(planets[planet1_pos+1:planet2_pos]) + tuple(planets[planet2_pos+1:])
    elif planet2_pos < sun_pos < planet1_pos:
        return tuple(planets[planets.index(planet1):planets.index(planet2)+1]) + tuple(planets[planets.index(planet2)+1:])
    else:
        return tuple()
