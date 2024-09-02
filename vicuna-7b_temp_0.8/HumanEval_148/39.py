
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
    if not isinstance(planet1, str) or not isinstance(planet2, str):
        return tuple()
    if planet1 == "Mercury" and planet2 == "Mercury":
        return tuple()
    if not all(letter in planet1 for planet1 in (planet1, planet2)) or len(set(planet1).intersection(planet2)) > 1:
        return tuple()
    elif len(set(planet1).intersection(planet2)) > 1:
        planets = []
        for planet1 in (planet1, planet2):
            for planet2 in (planet1, planet2):
                planets.append(bf(planet1, planet2))
        return sorted(planets, key=lambda x: abs(planet1.distance(x)))
    else:
        if planet1 in (planet2, "Sun"):
            planets = []
            for planet2 in (planet1, planet2):
                for planet1 in (planet2, planet1):
                    planets.append(bf(planet1, planet2))
            return sorted(planets, key=lambda x: abs(planet1.distance(x)))
        elif planet2 in (planet1, "Sun"):
            planets = []
            for planet1 in (planet2, planet1):
                for planet2 in (planet1, planet2):
                    planets.append(bf(planet1, planet2))
            return sorted(planets, key=lambda x: abs(planet2.distance(x)))
        else:
            planets = []
            for planet1 in (planet1, planet2):
                for planet2 in (planet1, planet2):
                    planets.append(bf(planet1, planet2))
            return sorted(planets, key=lambda x: abs(planet1.distance(x)))
