# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class FAMEAdCampaignGroup(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isFAMEAdCampaignGroup = True
        super(FAMEAdCampaignGroup, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        adaccount_id = 'adaccount_id'
        adaccount_name = 'adaccount_name'
        buying_type = 'buying_type'
        campaign_id = 'campaign_id'
        campaign_name = 'campaign_name'
        campaign_status = 'campaign_status'
        objective = 'objective'
        spend_cap = 'spend_cap'
        id = 'id'

    class DatePreset:
        today = 'today'
        yesterday = 'yesterday'
        this_month = 'this_month'
        last_month = 'last_month'
        this_quarter = 'this_quarter'
        lifetime = 'lifetime'
        last_3d = 'last_3d'
        last_7d = 'last_7d'
        last_14d = 'last_14d'
        last_28d = 'last_28d'
        last_30d = 'last_30d'
        last_90d = 'last_90d'
        last_week_mon_sun = 'last_week_mon_sun'
        last_week_sun_sat = 'last_week_sun_sat'
        last_quarter = 'last_quarter'
        last_year = 'last_year'
        this_week_mon_today = 'this_week_mon_today'
        this_week_sun_today = 'this_week_sun_today'
        this_year = 'this_year'

    class EffectiveStatus:
        active = 'ACTIVE'
        paused = 'PAUSED'
        deleted = 'DELETED'
        pending_review = 'PENDING_REVIEW'
        disapproved = 'DISAPPROVED'
        preapproved = 'PREAPPROVED'
        pending_billing_info = 'PENDING_BILLING_INFO'
        campaign_paused = 'CAMPAIGN_PAUSED'
        archived = 'ARCHIVED'
        adset_paused = 'ADSET_PAUSED'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'date_preset': 'date_preset_enum',
            'time_range': 'Object',
        }
        enums = {
            'date_preset_enum': [
                'today',
                'yesterday',
                'this_month',
                'last_month',
                'this_quarter',
                'lifetime',
                'last_3d',
                'last_7d',
                'last_14d',
                'last_28d',
                'last_30d',
                'last_90d',
                'last_week_mon_sun',
                'last_week_sun_sat',
                'last_quarter',
                'last_year',
                'this_week_mon_today',
                'this_week_sun_today',
                'this_year',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=FAMEAdCampaignGroup,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'adaccount_id': 'string',
        'adaccount_name': 'string',
        'buying_type': 'string',
        'campaign_id': 'string',
        'campaign_name': 'string',
        'campaign_status': 'string',
        'objective': 'string',
        'spend_cap': 'string',
        'id': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['DatePreset'] = FAMEAdCampaignGroup.DatePreset.__dict__.values()
        field_enum_info['EffectiveStatus'] = FAMEAdCampaignGroup.EffectiveStatus.__dict__.values()
        return field_enum_info
