from django.db import models
from django.utils.html import format_html

class Extensions(models.Model):

	name = models.CharField(max_length = 50)
	description = models.TextField()
	authorName = models.CharField(max_length = 50)
	license = models.TextField()
	#pubDate = models.DateField(auto_now_add = True)
	docFile = models.FileField(upload_to = 'documents/%Y/%m/%d')


	class Meta:
		pass

	def __unicode__(self):
	    return self.name


class Screenshots(models.Model):
	extensions = models.ForeignKey(Extensions, related_name = 'screenshots')
	image = models.ImageField(upload_to = 'screenshots/%Y/%m/%d')
	title = models.CharField(max_length = 200)

	def __unicode__(self):
	    return self.title

class ReleaseNotes(models.Model):
	extensions = models.ForeignKey(Extensions, related_name = 'releasenotes')
	version_number = models.TextField()
	change_log = models.TextField()
	release_notes = models.TextField()

	def __unicode__(self):
		return self.version_number

#class Person(models.Model):

 #   first_name = models.CharField(max_length=50)
  #  last_name = models.CharField(max_length=50)
   # color_code = models.CharField(max_length=6)
    

    #def colored_name(self):
     #   return format_html('<span style="color: #{0};">{1} {2}</span>',
      #                     self.color_code,
       #                    self.first_name,
        #                   self.last_name)
    #colored_name.allow_tags = True 

    #def born_in_fifties(self):
     #   return self.birthday.strftime('%Y')[:3] == '195'
    #born_in_fifties.boolean = True

    #class Meta:
	#	pass

    #def __unicode__(self):
	 #   return self.first_name