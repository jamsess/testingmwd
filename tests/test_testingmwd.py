# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, education
# All rights reserved.
#

from mwdextension.extension import TestingmwdExtension


def test_process_asset_purchase_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TestingmwdExtension(client, logger, config)
    result = ext.process_asset_purchase_request(request)
    assert result.status == 'success'


def test_process_asset_change_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TestingmwdExtension(client, logger, config)
    result = ext.process_asset_change_request(request)
    assert result.status == 'success'


def test_process_asset_suspend_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TestingmwdExtension(client, logger, config)
    result = ext.process_asset_suspend_request(request)
    assert result.status == 'success'


def test_process_asset_resume_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TestingmwdExtension(client, logger, config)
    result = ext.process_asset_resume_request(request)
    assert result.status == 'success'


def test_process_asset_cancel_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TestingmwdExtension(client, logger, config)
    result = ext.process_asset_cancel_request(request)
    assert result.status == 'success'


def test_process_asset_adjustment_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TestingmwdExtension(client, logger, config)
    result = ext.process_asset_adjustment_request(request)
    assert result.status == 'success'


def test_validate_asset_purchase_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TestingmwdExtension(client, logger, config)
    result = ext.validate_asset_purchase_request(request)
    assert result.status == 'success'
    assert result.data == request


def test_validate_asset_change_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TestingmwdExtension(client, logger, config)
    result = ext.validate_asset_change_request(request)
    assert result.status == 'success'
    assert result.data == request


def test_process_tier_config_setup_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TestingmwdExtension(client, logger, config)
    result = ext.process_tier_config_setup_request(request)
    assert result.status == 'success'


def test_process_tier_config_change_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TestingmwdExtension(client, logger, config)
    result = ext.process_tier_config_change_request(request)
    assert result.status == 'success'


def test_process_tier_config_adjustment_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TestingmwdExtension(client, logger, config)
    result = ext.process_tier_config_adjustment_request(request)
    assert result.status == 'success'


def test_validate_tier_config_setup_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TestingmwdExtension(client, logger, config)
    result = ext.validate_tier_config_setup_request(request)
    assert result.status == 'success'
    assert result.data == request


def test_validate_tier_config_change_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TestingmwdExtension(client, logger, config)
    result = ext.validate_tier_config_change_request(request)
    assert result.status == 'success'
    assert result.data == request


def test_process_usage_file(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1, 'type': 'type', 'status': 'status'}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TestingmwdExtension(client, logger, config)
    result = ext.process_usage_file(request)
    assert result.status == 'success'


def test_process_new_listing_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1, 'type': 'type', 'state': 'state'}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TestingmwdExtension(client, logger, config)
    result = ext.process_new_listing_request(request)
    assert result.status == 'success'


def test_process_remove_listing_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1, 'type': 'type', 'state': 'state'}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TestingmwdExtension(client, logger, config)
    result = ext.process_remove_listing_request(request)
    assert result.status == 'success'
