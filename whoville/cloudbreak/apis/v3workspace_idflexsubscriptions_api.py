# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class V3workspaceIdflexsubscriptionsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_flex_subscription_in_workspace(self, workspace_id, **kwargs):
        """
        create Flex subscription in workspace
        Flex subscriptions could be configured.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_flex_subscription_in_workspace(workspace_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param FlexSubscriptionRequest body:
        :return: FlexSubscriptionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_flex_subscription_in_workspace_with_http_info(workspace_id, **kwargs)
        else:
            (data) = self.create_flex_subscription_in_workspace_with_http_info(workspace_id, **kwargs)
            return data

    def create_flex_subscription_in_workspace_with_http_info(self, workspace_id, **kwargs):
        """
        create Flex subscription in workspace
        Flex subscriptions could be configured.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_flex_subscription_in_workspace_with_http_info(workspace_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param FlexSubscriptionRequest body:
        :return: FlexSubscriptionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_flex_subscription_in_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params) or (params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `create_flex_subscription_in_workspace`")


        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v3/{workspaceId}/flexsubscriptions', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FlexSubscriptionResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_flex_subscription_in_workspace(self, workspace_id, name, **kwargs):
        """
        delete Flex subscription by name in workspace
        Flex subscriptions could be configured.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_flex_subscription_in_workspace(workspace_id, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str name: (required)
        :return: FlexSubscriptionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_flex_subscription_in_workspace_with_http_info(workspace_id, name, **kwargs)
        else:
            (data) = self.delete_flex_subscription_in_workspace_with_http_info(workspace_id, name, **kwargs)
            return data

    def delete_flex_subscription_in_workspace_with_http_info(self, workspace_id, name, **kwargs):
        """
        delete Flex subscription by name in workspace
        Flex subscriptions could be configured.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_flex_subscription_in_workspace_with_http_info(workspace_id, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str name: (required)
        :return: FlexSubscriptionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_flex_subscription_in_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params) or (params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `delete_flex_subscription_in_workspace`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `delete_flex_subscription_in_workspace`")


        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v3/{workspaceId}/flexsubscriptions/{name}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FlexSubscriptionResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_flex_subscription_in_workspace(self, workspace_id, name, **kwargs):
        """
        get Flex subscription by name in workspace
        Flex subscriptions could be configured.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_flex_subscription_in_workspace(workspace_id, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str name: (required)
        :return: FlexSubscriptionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_flex_subscription_in_workspace_with_http_info(workspace_id, name, **kwargs)
        else:
            (data) = self.get_flex_subscription_in_workspace_with_http_info(workspace_id, name, **kwargs)
            return data

    def get_flex_subscription_in_workspace_with_http_info(self, workspace_id, name, **kwargs):
        """
        get Flex subscription by name in workspace
        Flex subscriptions could be configured.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_flex_subscription_in_workspace_with_http_info(workspace_id, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str name: (required)
        :return: FlexSubscriptionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_flex_subscription_in_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params) or (params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `get_flex_subscription_in_workspace`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_flex_subscription_in_workspace`")


        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v3/{workspaceId}/flexsubscriptions/{name}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FlexSubscriptionResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_flex_subscriptions_by_workspace(self, workspace_id, **kwargs):
        """
        list Flex subscriptions for the given workspace
        Flex subscriptions could be configured.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_flex_subscriptions_by_workspace(workspace_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :return: list[FlexSubscriptionResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_flex_subscriptions_by_workspace_with_http_info(workspace_id, **kwargs)
        else:
            (data) = self.list_flex_subscriptions_by_workspace_with_http_info(workspace_id, **kwargs)
            return data

    def list_flex_subscriptions_by_workspace_with_http_info(self, workspace_id, **kwargs):
        """
        list Flex subscriptions for the given workspace
        Flex subscriptions could be configured.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_flex_subscriptions_by_workspace_with_http_info(workspace_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :return: list[FlexSubscriptionResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_flex_subscriptions_by_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params) or (params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `list_flex_subscriptions_by_workspace`")


        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v3/{workspaceId}/flexsubscriptions', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[FlexSubscriptionResponse]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def put_default_flex_subscription_by_name_in_workspace(self, workspace_id, name, **kwargs):
        """
        sets the workspace default flag on the Flex subscription
        Flex subscriptions could be configured.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_default_flex_subscription_by_name_in_workspace(workspace_id, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.put_default_flex_subscription_by_name_in_workspace_with_http_info(workspace_id, name, **kwargs)
        else:
            (data) = self.put_default_flex_subscription_by_name_in_workspace_with_http_info(workspace_id, name, **kwargs)
            return data

    def put_default_flex_subscription_by_name_in_workspace_with_http_info(self, workspace_id, name, **kwargs):
        """
        sets the workspace default flag on the Flex subscription
        Flex subscriptions could be configured.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_default_flex_subscription_by_name_in_workspace_with_http_info(workspace_id, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_default_flex_subscription_by_name_in_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params) or (params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `put_default_flex_subscription_by_name_in_workspace`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `put_default_flex_subscription_by_name_in_workspace`")


        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v3/{workspaceId}/flexsubscriptions/setdefault/{name}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def put_used_for_controller_flex_subscription_by_name_in_workspace(self, workspace_id, name, **kwargs):
        """
        sets the workspace 'used for controller' flag on the Flex subscription
        Flex subscriptions could be configured.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_used_for_controller_flex_subscription_by_name_in_workspace(workspace_id, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.put_used_for_controller_flex_subscription_by_name_in_workspace_with_http_info(workspace_id, name, **kwargs)
        else:
            (data) = self.put_used_for_controller_flex_subscription_by_name_in_workspace_with_http_info(workspace_id, name, **kwargs)
            return data

    def put_used_for_controller_flex_subscription_by_name_in_workspace_with_http_info(self, workspace_id, name, **kwargs):
        """
        sets the workspace 'used for controller' flag on the Flex subscription
        Flex subscriptions could be configured.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_used_for_controller_flex_subscription_by_name_in_workspace_with_http_info(workspace_id, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_used_for_controller_flex_subscription_by_name_in_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params) or (params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `put_used_for_controller_flex_subscription_by_name_in_workspace`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `put_used_for_controller_flex_subscription_by_name_in_workspace`")


        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v3/{workspaceId}/flexsubscriptions/setusedforcontroller/{name}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
