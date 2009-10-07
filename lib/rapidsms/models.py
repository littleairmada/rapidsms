#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from django.db import models


class Backend(models.Model):
    """
    This model isn't really a backend. Those are regular Python classes, in
    rapidsms/backends/*. This is just a stub model to provide a primary key for
    each running backend, so other models can be linked to it with ForeignKeys.
    """

    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<%s: %s>' %\
            (type(self).__name__, self.name)


class App(models.Model):
    """
    This model isn't really a RapidSMS App. Like Backend, it's just a stub model
    to provide a primary key for each app, so other models can be linked to it.

    The Django ContentType stuff doesn't quite work here, since not all RapidSMS
    apps are valid Django apps. It would be nice to fill in the gaps and inherit
    from it at some point in the future.

    Instances of this model are generated by the update_apps management command,
    (which is hooked on Router startup (TODO: webui startup)), and probably
    shouldn't be messed with after that.
    """

    module = models.CharField(max_length=100, unique=True)
    active = models.BooleanField()


    def __unicode__(self):
        return self.module

    def __repr__(self):
        return "repr"
        #return '<%s: %s>' %\
        #    (type(self).__name__, self.module)


class Connection(models.Model):
    """
    The connection model pairs a backend with an individual identity unique to
    that backend (eg. a phone number, email address, irc nickname), so RapidSMS
    app developers need not concern themselves with backends.
    """

    backend  = models.ForeignKey(Backend)
    identity = models.CharField(max_length=100)
