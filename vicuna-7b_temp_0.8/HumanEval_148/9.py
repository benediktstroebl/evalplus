
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
    if not isinstance(planet1,str):
        return ()
    if not isinstance(planet2,str):
        return ()
    if planet1 == "Mercury" or planet2 == "Mercury":
        return ()
    planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
    #sort by proximity to the sun
    planets.sort(key=lambda x: abs(planet1.index(x) - planet2.index(x)))
    result = tuple(planets[::-1])
    if len(result) == 0:
        return ()
    return result
