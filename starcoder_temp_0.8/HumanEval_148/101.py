
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
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    for i in range(len(planets)):
        if planet1 == planets[i]:
            num1 = i
        if planet2 == planets[i]:
            num2 = i
    if (num1 > 0 and num1 < 8) and (num2 > 0 and num2 < 8):
        out = tuple(planets[num1:num2+1])
        return out
    else:
        return ()
