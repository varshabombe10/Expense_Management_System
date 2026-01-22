from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'transaction_type', 'date')
    list_filter = ('user','transaction_type', 'date')
    search_fields = ('user__username', 'amount')

    actions = ['mark_as_reviewed', 'delete_selected']

    def mark_as_reviewed(self, request, queryset):
        queryset.update(status="Reviewed")  # Assuming a status field
        self.message_user(request, "Selected transactions marked as reviewed.")
    
    mark_as_reviewed.short_description = "Mark selected transactions as reviewed"

admin.site.register(Transaction, TransactionAdmin)

admin.site.site_header = "💰 Expense Manager Dashboard"
admin.site.site_title = "Expense Admin"
admin.site.index_title = "Manage Expenses Efficiently"
from django.contrib.auth.models import Group

admin.site.unregister(Group)  # Hide Groups section from Admin Panel
