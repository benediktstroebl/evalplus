
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
    #print(planet1, planet2)
    # check if the input is a valid planet name
    if not planet1.isalpha() or not planet2.isalpha():
        return ()
    # sort the planets
    planets = sorted((str(p) for p in (planet1, planet2) + (('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune') if (planet1, planet2) == (str(p), str(p)) else (planet1, planet2))), key=lambda x: (len(str(x)), x,))
    # check if the planets are in the correct order
    planets = sorted(planets, key=lambda x: (x[0], x[1]), reverse=True)
    return planets
