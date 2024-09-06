
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
    lst = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planets = {}
    planets['Mercury'] = 0
    planets['Venus'] = 1
    planets['Earth'] = 2
    planets['Mars'] = 3
    planets['Jupiter'] = 4
    planets['Saturn'] = 5
    planets['Uranus'] = 6
    planets['Neptune'] = 7
    p1 = planets[planet1]
    p2 = planets[planet2]
    if p1 == p2:
        return ()
    else:
        lst = lst[p1:p2 + 1]
        if lst[0] == planet1:
            lst.remove(lst[0])
        if lst[-1] == planet2:
            lst.remove(lst[-1])
        return tuple(lst)
