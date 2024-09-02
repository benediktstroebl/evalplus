
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
    # sort the planets by proximity to the sun
    planets = (["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
               if "Mercury" in planet1 and "Mercury" in planet2
               else [])
    planets.extend([p for p in [planet2, planet1] if p in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]])
    # find the planets between the orbits of planet1 and planet2
    common_planets = [p for p in planets if (p < planet1 and p > planet2) or (p < planet2 and p > planet1)]
    # sort the common planets by proximity to the sun
    common_planets = sorted(common_planets, key=lambda p: (sun_distance(p), p.name))
    return common_planets
