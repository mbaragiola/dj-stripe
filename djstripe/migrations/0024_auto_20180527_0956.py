# Generated by Django 2.0.5 on 2018-05-27 06:56

from django.db import migrations, models
import django.db.models.deletion
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0023_auto_20180523_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('djstripe_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', djstripe.fields.StripeIdField(max_length=255, unique=True)),
                ('livemode', djstripe.fields.StripeNullBooleanField(default=None, help_text='Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.')),
                ('created', djstripe.fields.StripeDateTimeField(help_text='The datetime this object was created in stripe.', null=True)),
                ('metadata', djstripe.fields.StripeJSONField(blank=True, help_text='A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.', null=True)),
                ('description', djstripe.fields.StripeTextField(blank=True, help_text='A description of this object.', null=True)),
                ('djstripe_created', models.DateTimeField(auto_now_add=True)),
                ('djstripe_updated', models.DateTimeField(auto_now=True)),
                ('name', djstripe.fields.StripeCharField(help_text="The product's name, meant to be displayable to the customer. Applicable to both `service` and `good` types.", max_length=5000)),
                ('type', djstripe.fields.StripeCharField(choices=[('good', 'Good'), ('service', 'Service')], help_text='The type of the product. The product is either of type `good`, which is eligible for use with Orders and SKUs, or `service`, which is eligible for use with Subscriptions and Plans.', max_length=7)),
                ('active', djstripe.fields.StripeNullBooleanField(help_text='Whether the product is currently available for purchase. Only applicable to products of `type=good`.')),
                ('attributes', djstripe.fields.StripeJSONField(help_text='A list of up to 5 attributes that each SKU can provide values for (e.g., `["color", "size"]`). Only applicable to products of `type=good`.', null=True)),
                ('caption', djstripe.fields.StripeCharField(help_text='A short one-line description of the product, meant to be displayableto the customer. Only applicable to products of `type=good`.', max_length=5000, null=True)),
                ('deactivate_on', djstripe.fields.StripeJSONField(blank=True, help_text='An array of connect application identifiers that cannot purchase this product. Only applicable to products of `type=good`.')),
                ('images', djstripe.fields.StripeJSONField(blank=True, help_text='A list of up to 8 URLs of images for this product, meant to be displayable to the customer. Only applicable to products of `type=good`.')),
                ('package_dimensions', djstripe.fields.StripeJSONField(help_text='The dimensions of this product for shipping purposes. A SKU associated with this product can override this value by having its own `package_dimensions`. Only applicable to products of `type=good`.', null=True)),
                ('shippable', djstripe.fields.StripeNullBooleanField(help_text='Whether this product is a shipped good. Only applicable to products of `type=good`.')),
                ('url', djstripe.fields.StripeCharField(help_text='A URL of a publicly-accessible webpage for this product. Only applicable to products of `type=good`.', max_length=799, null=True)),
                ('statement_descriptor', djstripe.fields.StripeCharField(help_text="Extra information about a product which will appear on your customer's credit card statement. In the case that multiple products are billed at once, the first statement descriptor will be used. Only available on products of type=`service`.", max_length=22, null=True)),
                ('unit_label', djstripe.fields.StripeCharField(max_length=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='plan',
            name='aggregate_usage',
            field=djstripe.fields.StripeCharField(choices=[('last_during_period', 'Last during period'), ('last_ever', 'Last ever'), ('max', 'Max'), ('sum', 'Sum')], help_text='Specifies a usage aggregation strategy for plans of usage_type=metered. Allowed values are `sum` for summing up all usage during a period, `last_during_period` for picking the last usage record reported within a period, `last_ever` for picking the last usage record ever (across period bounds) or max which picks the usage record with the maximum reported usage during a period. Defaults to `sum`.', max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='billing_scheme',
            field=djstripe.fields.StripeCharField(choices=[('per_unit', 'Per unit'), ('tiered', 'Tiered')], help_text='Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in amount) will be charged per unit in quantity (for plans with `usage_type=licensed`), or per unit of total usage (for plans with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the tiers and tiers_mode attributes.', max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='nickname',
            field=djstripe.fields.StripeCharField(help_text='A brief description of the plan, hidden from customers.', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='tiers',
            field=djstripe.fields.StripeJSONField(help_text='Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`.', null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='tiers_mode',
            field=djstripe.fields.StripeCharField(choices=[('graduated', 'Graduated'), ('volume', 'Volume-based')], help_text='Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows.', max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='transform_usage',
            field=djstripe.fields.StripeJSONField(help_text='Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`.', null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='usage_type',
            field=djstripe.fields.StripeCharField(choices=[('licensed', 'Licensed'), ('metered', 'Metered')], default='licensed', help_text='Configures how the quantity per period should be determined, can be either`metered` or `licensed`. `licensed` will automatically bill the `quantity` set for a plan when adding it to a subscription, `metered` will aggregate the total usage based on usage records. Defaults to `licensed`.', max_length=8),
        ),
        migrations.AddField(
            model_name='plan',
            name='product',
            field=models.ForeignKey(help_text='The product whose pricing this plan determines.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='djstripe.Product'),
        ),
    ]
