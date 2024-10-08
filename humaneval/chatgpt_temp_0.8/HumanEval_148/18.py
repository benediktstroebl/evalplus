def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    start = planets.index(planet1)
    end = planets.index(planet2)
    if start > end:
        start, end = end, start
    return tuple(sorted(planets[start+1:end], key=lambda x: planets.index(x)))
