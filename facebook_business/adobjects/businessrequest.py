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

class BusinessRequest(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isBusinessRequest = True
        super(BusinessRequest, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        accessor = 'accessor'
        creation_time = 'creation_time'
        id = 'id'
        object_id = 'object_id'
        object_type = 'object_type'
        permitted_tasks = 'permitted_tasks'
        request_status = 'request_status'
        request_type = 'request_type'
        requestor = 'requestor'

    class ObjectType:
        page = 'PAGE'
        ad_account = 'AD_ACCOUNT'
        product_catalog = 'PRODUCT_CATALOG'
        app = 'APP'
        pixel = 'PIXEL'
        system_user = 'SYSTEM_USER'
        brand = 'BRAND'
        user = 'USER'
        project = 'PROJECT'
        instagram_account = 'INSTAGRAM_ACCOUNT'
        atlas_advertiser = 'ATLAS_ADVERTISER'
        funding_source = 'FUNDING_SOURCE'
        legacy_login = 'LEGACY_LOGIN'
        business_request = 'BUSINESS_REQUEST'
        example_cat = 'EXAMPLE_CAT'
        monetization_property = 'MONETIZATION_PROPERTY'
        grp_plan = 'GRP_PLAN'
        persona = 'PERSONA'
        credit_partition = 'CREDIT_PARTITION'
        payout_account = 'PAYOUT_ACCOUNT'
        ad_study = 'AD_STUDY'
        saved_audience = 'SAVED_AUDIENCE'
        custom_audience = 'CUSTOM_AUDIENCE'
        platform_custom_audience = 'PLATFORM_CUSTOM_AUDIENCE'
        event_source_group = 'EVENT_SOURCE_GROUP'
        offline_conversion_data_set = 'OFFLINE_CONVERSION_DATA_SET'
        ad_image = 'AD_IMAGE'
        photo = 'PHOTO'
        block_list = 'BLOCK_LIST'
        finance = 'FINANCE'
        ip = 'IP'
        credit_partition_config = 'CREDIT_PARTITION_CONFIG'
        video_asset = 'VIDEO_ASSET'
        business_unit = 'BUSINESS_UNIT'
        page_for_locations = 'PAGE_FOR_LOCATIONS'
        ad_account_creation_request = 'AD_ACCOUNT_CREATION_REQUEST'
        reseller_vetting_oe_request = 'RESELLER_VETTING_OE_REQUEST'
        registered_trademark = 'REGISTERED_TRADEMARK'
        custom_conversion = 'CUSTOM_CONVERSION'
        leads_access = 'LEADS_ACCESS'
        spaco_ds_data_collection = 'SPACO_DS_DATA_COLLECTION'
        owned_domain = 'OWNED_DOMAIN'
        whatsapp_business_account = 'WHATSAPP_BUSINESS_ACCOUNT'
        business_resource_group = 'BUSINESS_RESOURCE_GROUP'
        hotel_price_fetcher_pull_config = 'HOTEL_PRICE_FETCHER_PULL_CONFIG'
        news_page = 'NEWS_PAGE'
        place_page_set = 'PLACE_PAGE_SET'
        business_locations_wrapper = 'BUSINESS_LOCATIONS_WRAPPER'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessRequest,
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
        'accessor': 'Business',
        'creation_time': 'datetime',
        'id': 'string',
        'object_id': 'string',
        'object_type': 'string',
        'permitted_tasks': 'list<string>',
        'request_status': 'string',
        'request_type': 'string',
        'requestor': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ObjectType'] = BusinessRequest.ObjectType.__dict__.values()
        return field_enum_info
