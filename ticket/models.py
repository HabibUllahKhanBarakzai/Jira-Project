from api.models import TimeHistory, Member
from django.contrib.postgres.fields import JSONField
from django.db import models
import uuid


class Ticket(models.Model):
    DEFAULT_STATUS_IS_NOT_ASSIGNED = 0
    IS_ASSIGNED = 1
    IN_PROGRESS = 2
    DONE = 3
    TESTING = 4
    RESOLVED = 5

    STATUS = (
        (DEFAULT_STATUS_IS_NOT_ASSIGNED, "Not Assigned"),
        (IS_ASSIGNED, "Assigned"),
        (IN_PROGRESS, "In progress"),
        (DONE, "Done"),
        (TESTING, "Testing"),
        (RESOLVED, "Resolved")
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=100)
    status = models.SmallIntegerField(choices=STATUS, default=DEFAULT_STATUS_IS_NOT_ASSIGNED)
    sprint = models.ForeignKey("Sprint", on_delete=models.CASCADE, related_name="tickets", null=True)
    created_by = models.ForeignKey(Member, on_delete=models.SET_NULL,
                                   related_name="tickets_created", null=True)
    currently_assigned_to = models.ForeignKey(Member, on_delete=models.SET_NULL,
                                              related_name="current_tickets", null=True)


class Sprint(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    created_by = models.ForeignKey(Member, on_delete=models.SET_NULL,
                                   related_name="sprints_created", null=True)


class TicketHistory(TimeHistory):
    updated_by = models.ForeignKey(Member, on_delete=models.SET_NULL,
                                   related_name="ticket_updated", null=True)
    ticket = models.ForeignKey("Ticket", on_delete=models.CASCADE, related_name="history")