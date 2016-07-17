from __future__ import unicode_literals

from django.db import models

class MyModel2(models.Model):
	name = models.CharField(max_length=45)

	def __unicode__(self):
		return self.name
	# end def
# end class


class MyModel(models.Model):
	name = models.CharField(max_length=45)
	ref = models.ForeignKey(MyModel2)
# end class

