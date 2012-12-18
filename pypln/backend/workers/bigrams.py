# coding: utf-8
#
# Copyright 2012 NAMD-EMAP-FGV
#
# This file is part of PyPLN. You can get more information at: http://pypln.org/.
#
# PyPLN is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyPLN is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyPLN.  If not, see <http://www.gnu.org/licenses/>.

from pypelinin import Worker

import nltk
from nltk.collocations import BigramCollocationFinder
import cPickle



class Bigrams(Worker):
    """
    Returns pickled bigram finder
    """
    requires = ['tokens']
    bigram_measures = nltk.collocations.BigramAssocMeasures()

    def process(self, document):
        bigram_finder = BigramCollocationFinder.from_words(document['tokens'])

        return {'bigram_finder': cPickle.dumps(bigram_finder)}
