
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
    #8 planets
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    #their orbit positions
    orbit = (1,2,3,4,5,6,7,8)
    #the orbit of the planet1
    p1 = orbit.index(planets.index(planet1))
    #the orbit of the planet2
    p2 = orbit.index(planets.index(planet2))
    #if planet1 or planet2 are not correct planet names
    if p1 == None or p2 == None:
        return ()
    #planet1 is the closest to the Sun, planet2 is the furthest to the Sun
    if p1 < p2:
        return tuple(planets[p1+1:p2])
    #planet2 is the closest to the Sun, planet1 is the furthest to the Sun
    if p2 < p1:
        return tuple(planets[p2+1:p1])
