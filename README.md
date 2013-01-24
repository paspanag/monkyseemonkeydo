monkyseemonkeydo
================

This is a random number based algorithm in to finding text patterns and mimicking that pattern to another text intput.

There is not current measurement of fitness for the resulting pattern.

notes to improve the design:

Transform to a simple genetic algorithm by comparing the parent to the child. The comparison can be made from these
criterias:

1. Letter by letter correspondence of input to output - The most fit mimicking pattern is the one that uses the most input letters and try to achieve a one-to-one correspondence between input and output
2. How far the letter shifts with the alphabet range - the smaller the distance, the fitter the transform

