
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
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet1 = planet1.capitalize()
    planet2 = planet2.capitalize()
    if planet1 != planet2:
        if planet1 in planets and planet2 in planets:
            # star dist
            star = 149597870700
            x1, y1, z1 = e(planet1, star)
            x2, y2, z2 = e(planet2, star)
            # planet dist
            p1 = math.sqrt(x1**2 + y1**2 + z1**2)
            p2 = math.sqrt(x2**2 + y2**2 + z2**2)
            # check for planets within range
            planets = []
            if p1 < p2:
                range = p1
            else:
                range = p2
            for i in planets:
                if range > e(i, star):
                    planets.append(i)
            planets = tuple(planets)
            return planets
        else:
            return tuple()
    else:
        return tuple()
