
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
    # Hint: you can use the function built-in `sorted`
    def orbits(s):
        return {'Sun' : 0,
                'Mercury' : 1,
                'Venus' : 2,
                'Earth' : 3,
                'Mars' : 4,
                'Jupiter' : 5,
                'Saturn' : 6,
                'Uranus' : 7,
                'Neptune' : 8
                }[s]

    def bf1(planet1, planet2):
        ps1 = orbits(planet1)
        ps2 = orbits(planet2)
        planets = []
        for p in range(ps1, ps2+1):
            planets.append(nodes[p])
        return tuple(sorted(planets, key=lambda x: orbits(x)))

    planets = map(lambda p: nodes[orbits(p)], (planet1, planet2))
    return tuple(sorted(planets, key=lambda x: orbits(x)))

