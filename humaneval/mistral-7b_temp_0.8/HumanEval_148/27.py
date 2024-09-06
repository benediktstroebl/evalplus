
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
    # Put your solution here
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 in planets and planet2 in planets:
        if planet1 == planet2:
            return tuple()
        if planet1 == "Mercury":
            return tuple(planets[1:5])
        if planet1 == "Venus":
            return tuple(planets[2:7])
        if planet1 == "Earth":
            return tuple(planets[3:8])
        if planet1 == "Mars":
            return tuple(planets[4:8])
        if planet1 == "Jupiter":
            return tuple(planets[5:8])
        if planet1 == "Saturn":
            return tuple(planets[6:8])
        if planet1 == "Uranus":
            return tuple(planets[7:8])
        if planet1 == "Neptune":
            return tuple(planets[8:8])
    else
