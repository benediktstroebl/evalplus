
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

    if planet1.lower() in ("mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"):
        if planet2.lower() in ("mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"):
            planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
            planet1 = planet1.lower()
            planet2 = planet2.lower()
            for i in planets:
                if planet1 == i:
                    planet1 = planets.index(planet1)
                    break
            for i in planets:
                if planet2 == i:
                    planet2 = planets.index(planet2)
                    break
            planet1 = planet1 + 1
            planet2 = planet2 + 1
            sorted_planets = []
            while planet1 < planet2:
                sorted_planets.append(planets[planet1])
                
