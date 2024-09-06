
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
    planets_name = "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune".split()
    planets_orbit = range(8)
    names_orbit = dict(zip(planets_name, planets_orbit))
    if planet1 in names_orbit.keys() and planet2 in names_orbit.keys():
        planet1_orbit = names_orbit[planet1]
        planet2_orbit = names_orbit[planet2]
        planets_between = sorted(names_orbit.keys(), key=lambda k:abs(names_orbit[k]-planet1_orbit)+abs(names_orbit[k]-planet2_orbit))
        return tuple(planets_between[planet1_orbit:planet2_orbit])
    else:
        return tuple()
