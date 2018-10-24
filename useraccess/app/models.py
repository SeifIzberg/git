from django.db import models
from django.contrib.auth.models import Group, User, Permission


# Create your models here.

class MainTestObject(models.Model):

    #Method returns if user can apply low (type boolean)
    def can_be(self, permission, username):
        #Recovered user in database
        user = User.objects.get(username=username)
        #Recovered permission in database
        permission = Permission.objects.get(name=permission)

        user_all_group=user.groups.all()
        list_user_grou_id=[]
        for group in user_all_group:
            list_user_grou_id.append(group.id)
        allow = AllowPolicy.objects.filter(id__in=list_user_grou_id)
        allow_user = AllowPolicy.objects.filter(user_id=user.id)
        allow_policies=list(allow)+list(allow_user)
        for policy in allow_policies:
            # Recovered resource of allowPolicy
            allow_resource=policy.resource.split(":")

            # Retrieves the object type in resource applicable to allowPolicy
            if allow_resource[0]==str(type(self)):

                if allow_resource[1]=='*' or allow_resource[1]==str(self.id):

                    allow_permissions=policy.permission.split(" ")
                    for perm in allow_permissions:

                        if perm==permission.codename:

                            return True
        return False

    class Meta:
        abstract = True


class MyTestObject(MainTestObject):
    name = models.CharField(max_length=255)


class MyOtherTestObject(MainTestObject):
    name = models.CharField(max_length=255)


class AllowPolicy(models.Model):
    name = models.CharField(max_length=255)
    permission = models.CharField(max_length=255)
    resource = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

#Group.objects.filter(user__username="Kevin")