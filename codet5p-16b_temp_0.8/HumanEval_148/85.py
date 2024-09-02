
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

    if planet1.lower() not in ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"] or planet2.lower() not in ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]:
        return ()
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]
    orbit = 0
    start_planet = None
    end_planet = None
    for planet in planets:
        if planet == planet1:
            orbit = planets.index(planet)
            start_planet = planet
        if planet == planet2:
            orbit = planets.index(planet)
            end_planet = planet
    if orbit == 0:
        return ()
    if orbit > planets.index(start_planet):
        return ()
    if orbit < planets.
