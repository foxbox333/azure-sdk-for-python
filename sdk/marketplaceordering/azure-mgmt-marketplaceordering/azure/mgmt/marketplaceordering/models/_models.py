# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Resource(msrest.serialization.Model):
    """ARM resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class AgreementTerms(Resource):
    """Terms properties for provided Publisher/Offer/Plan tuple.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param publisher: Publisher identifier string of image being deployed.
    :type publisher: str
    :param product: Offer identifier string of image being deployed.
    :type product: str
    :param plan: Plan identifier string of image being deployed.
    :type plan: str
    :param license_text_link: Link to HTML with Microsoft and Publisher terms.
    :type license_text_link: str
    :param privacy_policy_link: Link to the privacy policy of the publisher.
    :type privacy_policy_link: str
    :param retrieve_datetime: Date and time in UTC of when the terms were accepted. This is empty
     if Accepted is false.
    :type retrieve_datetime: str
    :param signature: Terms signature.
    :type signature: str
    :param accepted: If any version of the terms have been accepted, otherwise false.
    :type accepted: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'publisher': {'key': 'properties.publisher', 'type': 'str'},
        'product': {'key': 'properties.product', 'type': 'str'},
        'plan': {'key': 'properties.plan', 'type': 'str'},
        'license_text_link': {'key': 'properties.licenseTextLink', 'type': 'str'},
        'privacy_policy_link': {'key': 'properties.privacyPolicyLink', 'type': 'str'},
        'retrieve_datetime': {'key': 'properties.retrieveDatetime', 'type': 'str'},
        'signature': {'key': 'properties.signature', 'type': 'str'},
        'accepted': {'key': 'properties.accepted', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AgreementTerms, self).__init__(**kwargs)
        self.publisher = kwargs.get('publisher', None)
        self.product = kwargs.get('product', None)
        self.plan = kwargs.get('plan', None)
        self.license_text_link = kwargs.get('license_text_link', None)
        self.privacy_policy_link = kwargs.get('privacy_policy_link', None)
        self.retrieve_datetime = kwargs.get('retrieve_datetime', None)
        self.signature = kwargs.get('signature', None)
        self.accepted = kwargs.get('accepted', None)


class ErrorResponse(msrest.serialization.Model):
    """Error response indicates Microsoft.MarketplaceOrdering service is not able to process the incoming request. The reason is provided in the error message.

    :param error: The details of the error.
    :type error: ~azure.mgmt.marketplaceordering.models.ErrorResponseError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponseError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class ErrorResponseError(msrest.serialization.Model):
    """The details of the error.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Error code.
    :vartype code: str
    :ivar message: Error message indicating why the operation failed.
    :vartype message: str
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponseError, self).__init__(**kwargs)
        self.code = None
        self.message = None


class Operation(msrest.serialization.Model):
    """Microsoft.MarketplaceOrdering REST API operation.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.marketplaceordering.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)


class OperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    :param provider: Service provider: Microsoft.MarketplaceOrdering.
    :type provider: str
    :param resource: Resource on which the operation is performed: Agreement, virtualmachine, etc.
    :type resource: str
    :param operation: Operation type: Get Agreement, Sign Agreement, Cancel Agreement etc.
    :type operation: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)


class OperationListResult(msrest.serialization.Model):
    """Result of the request to list MarketplaceOrdering operations. It contains a list of operations and a URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param value: List of Microsoft.MarketplaceOrdering operations supported by the
     Microsoft.MarketplaceOrdering resource provider.
    :type value: list[~azure.mgmt.marketplaceordering.models.Operation]
    :ivar next_link: URL to get the next set of operation list results if there are any.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = None
