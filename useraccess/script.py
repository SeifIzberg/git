from app.models import MyTestObject, MyOtherTestObject

object_1=MyTestObject.objects.get(id=1)
object_2=MyOtherTestObject.objects.get(id=1)
print("_____________________________________________________________")
print("_____________________________________________________________")
print("                     TEST ACCESS USER                        ")
print("_____________________________________________________________")
print("_____________________________________________________________")
print("object_1.can_be(update, john) -> True")
print("Result : "+str(object_1.can_be("update", "John")))
print("_____________________________________________________________"+"\n")
print("object_1.can_be(update, kevin) -> True")
print("Result : "+str(object_1.can_be("update","Kevin")))
print("_____________________________________________________________"+"\n")
print("object_1.can_be(update, nicolas) -> False")
print("Result : "+str(object_1.can_be("update", "Nicolas")))
print("_____________________________________________________________"+"\n")
print("object_2.can_be(update, hugo) -> True")
print("Result : "+str(object_2.can_be("update", "Hugo")))
print("_____________________________________________________________"+"\n")
print("object_2.can_be(update, kevin) -> False")
print("Result : "+str(object_2.can_be("update", "Kevin")))
print("_____________________________________________________________"+"\n")
print("object_2.can_be(update, nicolas) -> False")
print("Result : "+str(object_2.can_be("update", "Nicolas")))
print("_____________________________________________________________"+"\n")
print("object_2.can_be(read, hugo) -> True")
print("Result : "+str(object_2.can_be("read", "Hugo")))
print("_____________________________________________________________"+"\n")
print("object_2.can_be(read, kevin) -> False")
print("Result : "+str(object_2.can_be("read", "Kevin")))
print("_____________________________________________________________"+"\n")
print("object_2.can_be(read, nicolas) -> True")
print("Result : "+str(object_2.can_be("read", "Nicolas")))
print("_____________________________________________________________"+"\n")


#Preambule
#from app.models import *
#from django.contrib.auth.models import User,Group,Permission
#from django.contrib.contenttypes.models import ContentType

#Create users
#user = User.objects.create_user("Hugo",password="aaaa")

#Create group
#my_group , created=Group.objects.get_or_create(name="admin")

#Add user to group
#user1=User.objects.get(username="Kevin")
#user1.groups.add(my_group)

#Create permission
#contentType=ContentType.objects.get_for_model(User)
#permission=Permission.objects.create(codename="read",name="read",contentType=contentType)

#Create AllowPolicy
#allowPolicy=AllowPolicy.objects.create(name="Policy MyTestObject",permission="read update delete",user_id=User.objects.get(username="Nicolas").id,resource=str(type(object_1))+":"+str(object_1.id))